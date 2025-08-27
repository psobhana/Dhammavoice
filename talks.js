
//Share icon
function sharePage(videoID2) {
      const url = 'https://www.youtube.com/watch?v=' + videoID2;

      if (navigator.share) {
        navigator.share({
          title: document.title,
          text: "",
          url: url
        })
        .then(() => console.log(""))
        .catch((error) => console.log("Error sharing:", error));
      } else {
        navigator.clipboard.writeText(url).then(() => {
          alert("Link copied to clipboard!");
        });
      }
    }


//Search begin

// floating search box
document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("toggleSearchBtn");
  const floatingBox = document.getElementById("floatingSearch");

  toggleBtn.addEventListener("click", function () {
    if (floatingBox.style.display === "none") {
      floatingBox.style.display = "block";
    } else {
      floatingBox.style.display = "none";
    }
  });
});

// search

document.addEventListener("DOMContentLoaded", function () {
  let searchIndex = -1;
  let matches = [];
  let searchInput = document.getElementById("searchText");
  let counter = document.getElementById("counter");

  function clearHighlights() {
    let marks = document.querySelectorAll("mark.search-highlight");
    marks.forEach(m => {
      let parent = m.parentNode;
      parent.replaceChild(document.createTextNode(m.textContent), m);
      parent.normalize();
    });
  }

  function highlightAll(text) {
    clearHighlights();
    matches = [];
    searchIndex = -1;
    if (!text) {
      counter.textContent = "0 of 0";
      return;
    }

    let regex = new RegExp(text, "gi");
    let walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);

    while (walker.nextNode()) {
      let node = walker.currentNode;
      if (node.parentNode && !["SCRIPT", "STYLE"].includes(node.parentNode.nodeName)) {
        let match;
        while ((match = regex.exec(node.textContent))) {
          let mark = document.createElement("mark");
          mark.className = "search-highlight";
          let start = match.index;
          let end = regex.lastIndex;
          let before = node.textContent.slice(0, start);
          let middle = node.textContent.slice(start, end);
          let after = node.textContent.slice(end);
          let afterNode = document.createTextNode(after);
          mark.textContent = middle;
          let frag = document.createDocumentFragment();
          if (before) frag.appendChild(document.createTextNode(before));
          frag.appendChild(mark);
          frag.appendChild(afterNode);
          node.parentNode.replaceChild(frag, node);
          walker.currentNode = afterNode;
          matches.push(mark);
        }
      }
    }
    counter.textContent = matches.length ? `1 of ${matches.length}` : "0 of 0";
  }

  function scrollToMatch(i) {
    if (matches.length > 0) {
      matches.forEach(m => m.classList.remove("active-match"));
      matches[i].classList.add("active-match");
      matches[i].scrollIntoView({ behavior: "smooth", block: "center" });
      counter.textContent = `${i + 1} of ${matches.length}`;
    }
  }

  document.getElementById("btnSearch").addEventListener("click", function () {
    highlightAll(searchInput.value.trim());
    if (matches.length > 0) {
      searchIndex = 0;
      scrollToMatch(searchIndex);
    }
  });

  document.getElementById("btnNext").addEventListener("click", function () {
    if (matches.length > 0) {
      searchIndex = (searchIndex + 1) % matches.length;
      scrollToMatch(searchIndex);
    }
  });

  document.getElementById("btnPrev").addEventListener("click", function () {
    if (matches.length > 0) {
      searchIndex = (searchIndex - 1 + matches.length) % matches.length;
      scrollToMatch(searchIndex);
    }
  });
});

//Search end

//Youtube loaders

let currentVideoUrl = ""; // store current video link

function loadYoutube2(videoID) {
    var playerDiv = document.getElementById("player");
    currentVideoUrl = 'https://www.youtube.com/watch?v=' + videoID;

    playerDiv.innerHTML = `
        <iframe class="responsive-iframe" 
                src="https://www.youtube.com/embed/${videoID}?autoplay=1" 
                frameborder="0" 
                allowfullscreen>
        </iframe>
    `;
	// Show the share button after video loads
    document.getElementById("shareBtn").style.display = "inline-block";
}

function shareVideo() {
    if (!currentVideoUrl) {
        alert("No video loaded yet!");
        return;
    }

    if (navigator.share) {
        navigator.share({
            url: currentVideoUrl
        }).catch(err => console.log('Share failed:', err));
    } else {
        navigator.clipboard.writeText(currentVideoUrl).then(() => {
            alert("Link copied to clipboard: " + currentVideoUrl);
        });
    }
}



function loadYoutubeStart(videoID, startTime) {
    var playerDiv = document.getElementById("player");
	currentVideoUrl = 'https://www.youtube.com/watch?v=' + videoID + '&autoplay=1&start=' + startTime;
    playerDiv.innerHTML = '<iframe class="responsive-iframe" src="https://www.youtube.com/embed/' + videoID + '?autoplay=1&start=' + startTime + '" frameborder="0" allowfullscreen></iframe>';
// Show the share button after video loads
    document.getElementById("shareBtn").style.display = "inline-block";
}

function loadYoutubeStartStop(videoID, startTime, stopTime) {
    var playerDiv = document.getElementById("player");
	currentVideoUrl = 'https://www.youtube.com/watch?v=' + videoID + '&autoplay=1&start=' + startTime + '&end=' + stopTime;
    var embedUrl = 'https://www.youtube.com/embed/' + videoID + '?autoplay=1&start=' + startTime + '&end=' + stopTime;
    playerDiv.innerHTML = '<iframe class="responsive-iframe" src="' + embedUrl + '" frameborder="0" allowfullscreen></iframe>';
// Show the share button after video loads
    document.getElementById("shareBtn").style.display = "inline-block";
} 


function loadYoutubeLoop(videoID, loop = false) {
    var playerDiv = document.getElementById("player");
currentVideoUrl = 'https://www.youtube.com/watch?v=' + videoID;
    // Construct the URL with the loop parameter if needed
    var loopParam = loop ? '&loop=1' : '';
    
    // Construct the playlist parameter
    var playlistParam = '&playlist=' + videoID;

    playerDiv.innerHTML = '<iframe class="responsive-iframe" src="https://www.youtube.com/embed/' + videoID + '?autoplay=1' + loopParam + playlistParam + '" frameborder="0" allowfullscreen></iframe>';
// Show the share button after video loads
    document.getElementById("shareBtn").style.display = "inline-block";
}



function loadYoutubePlaylistLoop(playlistID, loop = false) {
    var playerDiv = document.getElementById("player");
    currentVideoUrl = 'https://www.youtube.com/watch?v=' + playlistID;
    // Construct the URL with the loop parameter if needed
    var loopParam = loop ? '&loop=1' : '';   
    playerDiv.innerHTML = '<iframe class="responsive-iframe" src="https://www.youtube.com/embed/videoseries?list=' + playlistID + '&autoplay=1' + loopParam + '" frameborder="0" allowfullscreen></iframe>';
// Show the share button after video loads
    document.getElementById("shareBtn").style.display = "inline-block";
}




//menu bar
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
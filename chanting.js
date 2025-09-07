

//Search begin

// floating search box


document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("toggleSearchBtn");
  const floatingBox = document.getElementById("floatingSearch");
  const closeBtn = document.getElementById("closeSearch");
  

  // Toggle with the search button
  toggleBtn.addEventListener("click", function () {
    if (floatingBox.style.display === "none" || floatingBox.style.display === "") {
      floatingBox.style.display = "block";
    } else {
      floatingBox.style.display = "none";
    }
  });

  // Close with the x button
  closeBtn.addEventListener("click", function () {
    floatingBox.style.display = "none";
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
    let walker = document.createTreeWalker(
      document.body, 
      NodeFilter.SHOW_TEXT, 
      {
        acceptNode: function(node) {
          // Skip script and style elements
          if (node.parentNode.tagName === 'SCRIPT' || 
              node.parentNode.tagName === 'STYLE') {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }, 
      false
    );

    let node;
    while (node = walker.nextNode()) {
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

        // Expand parent tree menus
        expandParentTreeMenus(mark);
      }
    }

    counter.textContent = matches.length ? `1 of ${matches.length}` : "0 of 0";
  }

  function expandParentTreeMenus(element) {
    let parent = element.parentNode;
    while (parent) {
      // Expand any UL with class tree2
      if (parent.tagName === "UL" && parent.classList.contains("tree2")) {
        parent.classList.add("expanded");
        
        // Also expand parent LI elements to show the expanded tree
        let liParent = parent.parentNode;
        while (liParent && liParent.tagName === "LI") {
          liParent.classList.add("expanded");
          liParent = liParent.parentNode;
          if (liParent && liParent.tagName === "UL") {
            liParent.classList.add("expanded");
          }
        }
      }
      
      // Expand details elements
      if (parent.tagName === "DETAILS") {
        parent.open = true;
      }
      
      parent = parent.parentNode;
    }
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



//dark mode begin
   function setTheme(theme) {
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    }

    // Load saved theme
    document.addEventListener("DOMContentLoaded", function() {
      const savedTheme = localStorage.getItem('theme') || 'light';
      setTheme(savedTheme);
    });
//dark mode end




//Share icon begin
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
	
	function sharePageSrart(videoID2, startTime2) {
      const url = 'https://www.youtube.com/watch?v=' + videoID2 + '&autoplay=1&start=' + startTime2;

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
	
	function sharePageSrartStop(videoID2, startTime2, stopTime2) {
      const url = 'https://www.youtube.com/watch?v=' + videoID2 + '&autoplay=1&start=' + startTime2 + '&end=' + stopTime2;

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
	
	
	function sharePagePlaylist(videoID2) {
      const url = 'https://www.youtube.com/watch?v=&list=' + videoID2;

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
//Share icon end



//menu bar
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
//Left menu begin
function toggleNav() {
  const sidebar = document.getElementById("mySidebar");
  const main = document.getElementById("main");
  const menuBtn = document.getElementById("menuBtn");

  if (sidebar.style.width === "250px") {
    sidebar.style.width = "0";
    main.style.marginLeft = "0";
    menuBtn.textContent = "☰"; // menu
  } else {
    sidebar.style.width = "250px";
    main.style.marginLeft = "250px";
    menuBtn.textContent = "✖"; // close
  }
}

// Close sidebar when clicking outside

document.addEventListener("click", function(event) {
  const sidebar = document.getElementById("mySidebar");
  const main = document.getElementById("main");
  const menuBtn = document.getElementById("menuBtn");

  if (sidebar.style.width === "250px") {
    if (!sidebar.contains(event.target) && !menuBtn.contains(event.target)) {
      sidebar.style.width = "0";
      main.style.marginLeft = "0";
      menuBtn.textContent = "☰";
    }
  }
});

//Left menu end


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

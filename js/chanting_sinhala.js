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

//Search begin

document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("toggleSearchBtn");
  const floatingBox = document.getElementById("floatingSearch");
  const closeBtn = document.getElementById("closeSearch");
  const searchInput = document.getElementById("searchText");
  const replaceOutput = document.getElementById("replaceTextOutput");
  const counter = document.getElementById("counter");

  // =========================
  // Floating Search Box Toggle
  // =========================
  toggleBtn.addEventListener("click", () => {
    floatingBox.style.display =
      (floatingBox.style.display === "none" || floatingBox.style.display === "")
        ? "block" : "none";
  });
  closeBtn.addEventListener("click", () => floatingBox.style.display = "none");

  // =========================
  // Replace Function
  // =========================
  function replaceText() {
    const a = "\u0DCA"; // Sinhala sign (්)
    const b = "\u200D"; // Zero Width Joiner (‍)
    
    const specialCombinations = [
      "\u0D9A\u0DCA\u0D9A", // ක්ක
      "\u0D9A\u0DCA\u0DC2", // ක්ෂ
      "\u0DAD\u0DCA\u0DAE", // ත්ථ
      "\u0DAD\u0DCA\u0DC0", // ත්ව
      "\u0DB1\u0DCA\u0DC0", // න්ව
      "\u0DB1\u0DCA\u0DAD", // න්ථ
      "\u0DB1\u0DCA\u0DAF", // න්ද
      "\u0DB1\u0DCA\u0DB0"  // න්ධ
    ];

    const currentText = searchInput.value.normalize("NFD");
    let replacedText = currentText;
    let replacementCount = 0;

    for (const combination of specialCombinations) {
      const pattern = combination.normalize("NFD");
      const regex = new RegExp(pattern, "g");
      const matches = replacedText.match(regex);
      if (matches) replacementCount += matches.length;
      replacedText = replacedText.replace(regex, pattern.replace(a, a + b));
    }

    const remainingViramaRegex = new RegExp(a + "(?!" + b + ")", "g");
    const remainingMatches = replacedText.match(remainingViramaRegex);
    if (remainingMatches) {
      replacementCount += remainingMatches.length;
      replacedText = replacedText.replace(remainingViramaRegex, b + a);
    }

    replaceOutput.value = replacedText.normalize("NFC");

    if (replacementCount > 0) {
      counter.textContent = `${replacementCount} replacements made`;
    } else {
      counter.textContent = "No ◌් found";
    }

    setTimeout(() => { counter.textContent = "0 of 0"; }, 2000);
  }

  document.getElementById("btnReplace").addEventListener("click", replaceText);

  // =========================
  // Search & Highlight
  // =========================
  let searchIndex = -1;
  let matches = [];

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

        expandParentTreeMenus(mark);
      }
    }

    counter.textContent = matches.length ? `1 of ${matches.length}` : "0 of 0";
  }

  function expandParentTreeMenus(element) {
    let parent = element.parentNode;
    while (parent) {
      if (parent.tagName === "UL" && parent.classList.contains("tree2")) {
        parent.classList.add("expanded");
        let liParent = parent.parentNode;
        while (liParent && liParent.tagName === "LI") {
          liParent.classList.add("expanded");
          liParent = liParent.parentNode;
          if (liParent && liParent.tagName === "UL") {
            liParent.classList.add("expanded");
          }
        }
      }
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

/*
  document.getElementById("btnSearch").addEventListener("click", function () {
    highlightAll(searchInput.value.trim());
    if (matches.length > 0) {
      searchIndex = 0;
      scrollToMatch(searchIndex);
    }
  });
*/

  document.getElementById("btnSearch").addEventListener("click", function () {
    highlightAll(replaceOutput.value.trim());
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


/* ===== Dragging search box start ===== */
document.addEventListener("DOMContentLoaded", function () {
  const box=document.getElementById("floatingSearch");
  let isDragging=false, offsetX=0, offsetY=0;

  function startDrag(x,y) {
    isDragging=true;
    offsetX=x - box.getBoundingClientRect().left;
    offsetY=y - box.getBoundingClientRect().top;
    document.body.style.userSelect="none";
  }
  function doDrag(x,y) {
    if(!isDragging) return;
    box.style.left=(x-offsetX)+"px";
    box.style.top=(y-offsetY)+"px";
    box.style.right="auto";
  }
  function endDrag() {
    isDragging=false;
    document.body.style.userSelect="";
  }

  // Desktop
  box.addEventListener("mousedown",(e)=>{
    if(e.target.tagName==="INPUT"||e.target.tagName==="BUTTON"||e.target.tagName==="SPAN") return;
    startDrag(e.clientX,e.clientY);
  });
  document.addEventListener("mousemove",(e)=>doDrag(e.clientX,e.clientY));
  document.addEventListener("mouseup",endDrag);

  // Mobile
  box.addEventListener("touchstart",(e)=>{
    if(e.target.tagName==="INPUT"||e.target.tagName==="BUTTON"||e.target.tagName==="SPAN") return;
    let t=e.touches[0];
    startDrag(t.clientX,t.clientY);
  });
  document.addEventListener("touchmove",(e)=>{
    if(!isDragging) return;
    let t=e.touches[0];
    doDrag(t.clientX,t.clientY);
  },{passive:false});
  document.addEventListener("touchend",endDrag);
});

/* ===== Dragging search box end ===== */


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




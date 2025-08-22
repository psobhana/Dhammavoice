

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
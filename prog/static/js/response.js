function handleYesClick() {
    console.log('Yes clicked');
    fetch('/likeButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ response: 'Yes' })  // Send data to the server
    })
    .then(response => response.json())
    .catch(error => console.error('Error:', error));

    // Play the next song and potentially trigger the match animation
    nextSong();

    // 10% chance of triggering match animation and transition
    matchChance();
}

function handleNoClick() {
    console.log('No clicked');
    fetch('/likeButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ response: 'No' })  // Send data to the server
    })
    .then(response => response.json())
    .catch(error => console.error('Error:', error));

    // Play the next song
    nextSong();

    // 10% chance of triggering match animation and transition
    matchChance();
}

function matchChance() {
    // 10% chance of triggering match animation and transition
    if (Math.random() < 0.50) {
        document.getElementById("match-overlay").style.display = "flex";
        setTimeout(() => {
            window.location.href = "match.html";
        }, 2000);
    }
}
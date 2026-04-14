const cards = ["🂡", "🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂭", "🂮"];

function startKonkan() {
    let hand = "";
    for (let i = 0; i < 7; i++) {
        let rand = cards[Math.floor(Math.random() * cards.length)];
        hand += `<span style="font-size: 45px; background:white; color:black; margin:5px; padding:5px; border-radius:5px;">${rand}</span>`;
    }
    document.getElementById('konkan-display').innerHTML = hand;
    updateScore(15);
}

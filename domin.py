function playDomino() {
    let p1 = Math.floor(Math.random() * 7);
    let p2 = Math.floor(Math.random() * 7);
    document.getElementById('domino-display').innerHTML = `
        <div style="background:white; color:black; padding:15px; border-radius:10px; font-weight:bold; font-size:30px; border:3px solid #000;">
            ${p1} | ${p2}
        </div>
        <p style="color:var(--tmx-gold); font-weight:bold; margin-top:15px;">+10 خاڵ!</p>
    `;
    updateScore(10);
}

const sysData = [
    { c: "pkg update && pkg upgrade", m: "نوێکردنەوەی هەموو پاکێجەکان" },
    { c: "termux-setup-storage", m: "بەستنەوەی تێرمۆکس بە میمۆری مۆبایل" },
    { c: "apt list --installed", m: "بینینی هەموو ئەو ئامرازانەی دابەزێنراون" },
    { c: "top", m: "پیشاندانی پڕۆسەکانی ناو سیستم و بەکارهێنانی ڕام" },
    { c: "df -h", m: "زانینی بڕی جێگەی بەتاڵ لە میمۆری" }
];

const sysBox = document.getElementById('sys-data');
sysData.forEach(item => {
    sysBox.innerHTML += `<div class="cmd-item"><code class="cmd-text">${item.c}</code><span class="cmd-desc">// ${item.m}</span></div>`;
});

function openWin(id) { document.getElementById(id).style.display = 'flex'; }
function closeWin(id) { document.getElementById(id).style.display = 'none'; }

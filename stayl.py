:root { --tmx-green: #1db954; --tmx-red: #ff0000; --tmx-gold: #ffd700; }
body { background-color: #0c0c0c; color: white; font-family: sans-serif; text-align: center; margin: 0; }
.header { background-color: var(--tmx-red); padding: 15px; font-size: 22px; font-weight: bold; }
.tab-bar { display: flex; justify-content: space-around; background: #1a1a1a; padding: 12px; border-bottom: 2px solid #333; }
.tab { cursor: pointer; color: #888; font-weight: bold; }
.tab.active { color: var(--tmx-green); border-bottom: 2px solid var(--tmx-green); }
.game-container { display: none; padding: 20px; }
.game-container.active { display: block; }
.btn { background-color: var(--tmx-green); color: white; padding: 14px 28px; border-radius: 50px; border: none; cursor: pointer; font-weight: bold; margin: 10px; }
.score-box { background: #222; margin: 8px auto; padding: 15px; border-radius: 12px; border-right: 5px solid var(--tmx-green); display: flex; justify-content: space-between; max-width: 380px; }
input { padding: 15px; border-radius: 10px; background: #1a1a1a; color: white; border: 1px solid #444; width: 80%; text-align: center; }
.table-ui { border-radius: 20px; min-height: 200px; margin: 20px auto; max-width: 400px; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; padding: 20px; }

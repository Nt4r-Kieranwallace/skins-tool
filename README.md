<div align="center">

<img src="banner.jpg" alt="skins-data.py" width="100%">

# skins - tool

<p>An executable file for modifying <i><a href="https://en.wikipedia.org/wiki/Arena_of_Valor">Arena of Valor</a></i> game files, allowing users to create in-game skins for your favorite heroes.</p>

</div>

---

> [!CAUTION]
> **Mod_Tools.py** is a resource for creating skins data. It is carefully maintained and will receive general updates whenever the game updates.
> You can download and use it right away, but you will need to figure out how to run it yourself.
> Use **Python 3.9.7** to run certain scripts.

---

### 🖥️ Supported Platforms

> [!TIP]
> - [x] Windows
> - [x] Android

---

### 🧰 Tool Features

> [!WARNING]
> - [x] Skill effects
> - [x] Recall
> - [x] Haste
> - [x] Shadow effects
> - [x] Skin names
> - [x] Skin badges
> - [x] Change monster / turret buffs (Dimension Breaker)
> - [x] Skin background sounds
> - [x] Skin lobby sounds
> - [x] Skin models

---

### 🛠️ Download the Script

> [!IMPORTANT]
> - path: [script](https://github.com/Nt4r-Kieranwallace/skins-tool)
> - Make sure the files you want to work with actually exist, and that the script runner is compatible with its paired files.
> - Check that your original `Resources` folder is truly the original, unmodified version.
> - If you are not sure, use `Restore Original Game Data` in the game, re-download `Resources`, and then run `Mod_Tools.py`.

---

### 📂 Structure - Data in the folder [Resources]

> [!NOTE]
> File structure inside the `Resources` folder.

```
📦 Resources/ (MOD)
┃
┣━ 📂 Ages
┃   ┗━ 📂 Prefab_Characters
┃       ┗━ 📂 Prefab_Hero
┃           ┣─ 📄 Actor_{hero_id}_Actions.pkg.bytes
┃           ┗─ 📄 CommonActions.pkg.bytes
┃
┣━ 📂 Databin
┃   ┗━ 📂 Client
┃       ┣━ 📂 Actor
┃       ┃   ┣─ 📄 heroSkin.bytes
┃       ┃   ┗─ 📄 organSkin.bytes
┃       ┃
┃       ┣━ 📂 Huanhua
┃       ┃   ┗─ 📄 ResSkinExclusiveBattleEffectCfg.bytes
┃       ┃
┃       ┣━ 📂 Skill
┃       ┃   ┣─ 📄 liteBulletCfg.bytes
┃       ┃   ┗─ 📄 skillmark.bytes
┃       ┃
┃       ┗━ 📂 Sound
┃           ┣─ 📄 BattleBank.bytes
┃           ┣─ 📄 ChatSound.bytes
┃           ┣─ 📄 HeroSound.bytes
┃           ┣─ 📄 LobbyBank.bytes
┃           ┗─ 📄 LobbySound.bytes
┃
┗━ 📂 Prefab_Characters
    ┗─ 📄 Actor_{hero_id}_Infos.pkg.bytes
```

---

### 📲 Installing a Skin Mod Package

> [!TIP]
> 1. Extract `{files_name}.zip` (Mod).
> 2. Copy the contents into this path: `Android/data/com.garena.game.kgth/files/Resources/ver`
> 3. Overwrite the existing files, then open the game and check whether the Mod Skin works.

---

### 🚨 When the "Network Error" Message Appears

This happens when files were edited incorrectly or were not modified properly. It can affect any file.
The exception is when you have been playing for a long time without disconnecting and suddenly get kicked today. This usually happens close to an update, or during the major update window at **04:00 - 05:00**.
Remove the mod before playing. If you play during 04:00 - 05:00, the "Network Error" message will appear immediately.

<div align="center">

<img src="network-error.jpg" alt="Example of an unresolved issue" width="60%">

<sub>(Unresolved issue)</sub>

</div>

---

### ⚠️ Possible Causes

1. **In-game data** - There may be a bug or glitch that causes disconnections during play (for example, one team exploiting a bug).
2. **Incorrect internal skin data edits** - The data was not edited or checked thoroughly, so a "Network Error" slips in, or the data is outdated and has not been updated carefully.
3. **Incorrect file edits in folders** - `Ages` `AssetRefs` `Databin` `Model`

---

### 📜 Disclaimer

> [!CAUTION]
> - Modifying Arena of Valor violates the game's rules, and the game does not permit modification.
> - If your account gets banned, I take no responsibility whatsoever. By using `Mod_Tools.py`, you accept the risk yourself.

---

### 📄 Source Code

- Not ready for release at this time, and there are no plans to publish it until development of the script officially ends.

---

### 🖥️ License

This software is released under License 3.0. Full credit must be given when using it.

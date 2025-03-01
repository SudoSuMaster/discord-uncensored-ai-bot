# Discord AI Bot - ReadMe

## 🚨 Disclaimer
This Discord bot, along with its AI functionalities, is provided **solely for entertainment and educational purposes**. While the bot may assist with responses, **neither the creator nor the AI can be held responsible** for any actions taken based on its output. Like any tool, it should be used with **caution and awareness**. Users are encouraged to exercise **discretion and critical thinking** when interacting with the bot and to take responsibility for any outcomes resulting from its use.

---

## 🛠️ Ollama Setup
To run **Ollama** in Docker, use the following **Docker Compose file**:

🔗 [Ollama Docker Compose File](https://github.com/SudoSuMaster/docker-compose-files/blob/main/ollama-ai/docker-compose.yml)

### Steps:
1. Clone the repository or download the compose file.
2. Navigate to the directory where you saved the compose file.
3. Run the following command:
   ```bash
   docker compose up -d
   ```

---

## 🤖 Setting Up a Discord Bot

### 1️⃣ Go to the Discord Developer Portal
- Visit the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account.

### 2️⃣ Create a New Application
- Click on **"New Application"** and give it a name (this will be your bot’s name).
- Optionally, upload an icon and add a description.

### 3️⃣ Enable Bot Capabilities
- Navigate to the **Bot** tab.
- Enable the **"MESSAGE CONTENT INTENT"** toggle to allow the bot to read messages.

### 4️⃣ Generate a Bot Invite Link
- Go to the **OAuth2** tab.
- Under **"OAuth2 URL Generator"**, select **"bot"** under **SCOPES**.

  ![OAuth2](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/eab4acb2-e189-4546-8abd-59d02da40b31)

### 5️⃣ Configure Bot Permissions
- Scroll to the **"BOT PERMISSIONS"** section.
- Select the required permissions, such as:
  - ✅ **Send Messages**
  - ✅ **Read Message History**
  - ✅ **Read Messages** (or **View Channels**)

  ![Permissions](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/0a18b618-6833-4a46-a900-dc590931be1e)

### 6️⃣ Invite Your Bot to a Server
- After setting the permissions, a bot invite link will be generated.
- Copy the invite link and paste it into your browser to add the bot to your server.

  ![Invite Bot](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/a4f2b9cd-9dbe-4db0-95dd-bf8727e7e881)

---

## 🔑 Setting Up Your Discord Token

### Steps:
1. Rename **`.env.copy`** to **`.env`**.
2. Open the `.env` file and paste your **Discord Token** inside.
3. You can find your token in the Developer Portal:
   - Go to **Bot → Reset Token**.
   - **⚠️ Never share this token with anyone!**

   ![Discord Token](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/0897fbe9-6588-404e-b410-fd168eb749a9)

---

## 🌍 Ollama API Setup

### Steps:
1. Change the API URL in the configuration.

   ![API URL](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/af915dc7-41b1-4e6d-8270-549a8f220f3e)

2. To find your **API URL**:
   - Open **Ollama WebUI → Settings → General**.

   ![Find API URL](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/fbc41311-755a-4999-90ec-1d4c24200b78)

---

## 🚀 Running the Bot

1. Ensure that **Ollama** is running.
2. Run the bot with:
   ```bash
   python main.py
   ```

### **Note:**
- If you have a **GPU**, it will be used by default.
- If you don’t have a GPU, modify the **Docker Compose file** to use **CPU mode** instead.
- Check the **official documentation** for additional details on GPU/CPU configuration.

---

## 🎯 Enjoy Your AI-Powered Discord Bot! 🎯

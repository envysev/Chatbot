# Chatbot

4. How to Upload Your Project to GitHub (via Terminal)

Step-by-step:

Open terminal and go to your project folder
Example: cd path/to/groqchatbot

Initialize git (if not done)
git init

Stage all changes
git add .

Commit changes
git commit -m "Initial commit with GitHub OAuth and chatbot"

Add your remote repo (only if not yet set)
git remote add origin https://github.com/envysev/Chatbot.git

Push to GitHub
If no existing content:
git push -u origin main

If existing content causes a conflict:
git push -u origin main --force


echo "git clone, Please Wait..."
git clone https://github.com/Touka19/Fheroku.git /tgvc-userbot-dev
echo "Trying Requirements..."
cd /tgvc-userbot-dev
pip3 install -U -r requirements.txt
echo "Booting bot"
python3 main.py

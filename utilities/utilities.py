# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot

import os
import json
from pathlib import Path
import signal
import sys
import os
import time

import psutil

MODULE_DIR = Path(__file__).resolve().parents[1]
MASTER_CRYPTO_FARM_BOT_DIR = Path(__file__).resolve().parents[3]
sys.path.append(str(MASTER_CRYPTO_FARM_BOT_DIR))

from mcf_utils.database import Database


def getConfig(key, default=None):
    json_file = os.path.join(MODULE_DIR, "bot_settings.json")

    if not os.path.exists(json_file):
        return default

    with open(json_file, "r") as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return default


def is_module_disabled(bot_globals, log):
    try:
        db = Database(bot_globals["mcf_dir"] + "/database.db", log)
        module_name = bot_globals["module_name"]
        is_disabled = db.getSettings(f"{module_name}_disabled", "0") == "1"
        return is_disabled == True or is_disabled == "1"
    except Exception as e:
        log.error(f"Error while checking if module is disabled: {e}")
        return False


def kill_process():
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except Exception as e:
        pass
    try:
        os.kill(os.getpid(), signal.SIGTERM)
    except Exception as e:
        pass
    exit(0)


def clean_logs():
    try:
        log_file = os.path.join(MODULE_DIR, "bot.log")
        if not os.path.exists(log_file):
            return

        log_recent_file = os.path.join(MODULE_DIR, "bot_log_recent.log")
        if os.path.exists(log_recent_file):
            os.remove(log_recent_file)

        os.rename(log_file, log_recent_file)
    except Exception as e:
        pass


def kill_me():
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except Exception as e:
        pass
    try:
        os.kill(os.getpid(), signal.SIGTERM)
    except Exception as e:
        pass
    exit(0)


def check_mcf_status(log, mcf_pid, module_name):
    mcf_pid = int(mcf_pid)
    log.info("<green>Montoring MCF thread started</green>")
    try:
        while True:
            if not psutil.pid_exists(mcf_pid):
                log.error(
                    f"<red>MCF restarted or Closed. Killing {module_name} module</red>"
                )
                log.info("<green>Module stopped</green>")
                kill_me()
            time.sleep(1)
    except Exception as e:
        pass

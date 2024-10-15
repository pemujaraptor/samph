config = {
        "web_server": {
                "host": "0.0.0.0",
                "port": 54321,
        },
        "telegram_api": {
                "api_id": 28259465, # Must be integer/number, no " at start and end
                "api_hash": "7fa5c80200a45789ef874973cba5a766", # Must be string, don't forget " at start and end
        },
        "auto_update": True,
        "auto_update_modules": True,
        "update_check_interval": 3600,
        "run_delay": 30,
        "display_module_logs_in_console": False,
}
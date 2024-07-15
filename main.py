def main():
    from multi_agent_bot.ui.chat_ui import UI
    from multi_agent_bot.utils.logging import setup_logging
    
    setup_logging()
    ui = UI()
    ui.run()

if __name__ == "__main__":
    main()
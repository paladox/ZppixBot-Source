from sopel.module import rule

@rule('.*$nickname.*')
def ping_converse(bot, trigger):
    if trigger.nick == 'Reception123':
        bot.say("I get it, Reception123, talking to real people is too overrated.")
    elif trigger.nick == 'Reception|away':
        bot.say("I get it, Reception123, talking to real people is too overrated.")
    elif trigger.nick == 'PuppyKun':
        bot.say("Hit the tab button too soon again, PuppyKun? Tsk tsk tsk.")
    elif trigger.nick == 'wm-bot' or trigger.nick == 'Source-Zppixbot' or trigger.nick == 'wikibugs' or trigger.nick == 'wikibugs_':
        return  
    elif trigger.nick == 'Zppix':
        bot.say("Talking to your own AI bot again, are you Zppix?")
    else:
        bot.say("Hey, %s, I'm an AI which is too dumb to carry on a converstation perhaps, you meant to ping Zppix instead?" % trigger.nick)

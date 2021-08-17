from mycroft import MycroftSkill, intent_file_handler


class TestOverrideIdle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('idle.override.test.intent')
    def handle_idle_override_test(self, message):
        self.speak_dialog('idle.override.test')


def create_skill():
    return TestOverrideIdle()


class Label:

    @classmethod
    def get_msg(self, label) -> str:
        self.label = label
        self.message = None
        bindings = {
        "--improve" :   "👌 IMPROVE: ",
        "--new"     :   "📦 NEW: ",
        "--doc"    :   " 📖 DOC: ",
        "--fix"     :   "🐛 FIX: ",
        "--release" :   "🔖 "
        }

        for key, value in bindings.items():
            if self.label == key:
                self.message = value

        return self.message

    @classmethod
    def get_msg_from_num(self, num) -> str:
        self.num = num
        self.message = None
        bindings = {
            "-1"   :   "👌 IMPROVE: ",
            "-2"   :   "📦 NEW: ",
            "-3"   :   " 📖 DOC: ",
            "-4"   :   "🐛 FIX: ",
            "-5"   :   "🔖 "
                }

        for key, value in bindings.items():
            if self.num == key:
                self.message = value

        return self.message

from flox import Flox


class Template(Flox):
    def query(self, query):
        for _ in range(250):
            self.add_item(
                title=self.args,
                subtitle=str(_)
            )

    def context_menu(self, data):
        self.add_item(
            title=data,
            subtitle=data
        )


if __name__ == "__main__":
    template = Template()
    template.run()
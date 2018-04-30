from controller import Controller


class Chart:

    c = Controller()

    def do_chart(self, option):
        switcher =



class Bar(Chart):
    def print_chart(self):
        return self.c.print_chart_sales()


class Pie(Chart):
    def print_chart_pie(self):
        return self.c.print_chart_pie()


class Line(Chart):
    def print_chart_line(self):
        return self.c.print_chart_line()

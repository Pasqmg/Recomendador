from datamanager.ImageGetter import ImageGetter
from datamanager.Item import Item
import os.path

class RecommendedItem(Item):

    def __init__(self, id, title, ratio, genres):
        super().__init__(title, genres)
        self.id = id
        self.ratio = ratio

    def __lt__(self, other):
        if self.ratio > other.ratio:
            return self
        else:
            return other

    def get_year(self):
        try:
            string = self.title
            parts = string.split("(")
            title = parts[0]
            if len(parts) > 2:
                # part of the title is between brackets
                title = parts[0]+"("+parts[1]
                year = parts[2].split(")")[0]
            else:
                year = parts[1].split(")")[0]
            return year
        except IndexError:
            return "UNABLE TO LOAD YEAR"

    def get_title(self):
        try:
            string = self.title
            parts = string.split("(")
            title = parts[0]
            if len(parts) > 2:
                # part of the title is between brackets
                title = parts[0]+"("+parts[1]
                year = parts[2].split(")")[0]
            else:
                year = parts[1].split(")")[0]
            if "," in title:
                if "(" in title:
                    title_parts = title.split(",")
                    part_with_comma = title_parts[1]
                    final_parts = part_with_comma.split("(")
                    title = final_parts[0]+title_parts[0]+" ("+final_parts[1]
                else:
                    title_parts = title.split(",")
                    title = title_parts[1]+title_parts[0]

            return title
        except IndexError:
            return self.title

    def print(self):
        try:
            string = self.title
            parts = string.split("(")
            title = parts[0]
            if len(parts) > 2:
                # part of the title is between brackets
                title = parts[0]+"("+parts[1]
                year = parts[2].split(")")[0]
            else:
                year = parts[1].split(")")[0]
            if "," in title:
                if "(" in title:
                    title_parts = title.split(",")
                    part_with_comma = title_parts[1]
                    final_parts = part_with_comma.split("(")
                    title = final_parts[0]+title_parts[0]+" ("+final_parts[1]
                else:
                    title_parts = title.split(",")
                    title = title_parts[1]+title_parts[0]

            #print(title, year, self.ratio)
            # download and save image if necessary
            #if not os.path.exists("/home/pasqual/PycharmProjects/Recomendador/images/" + title + ".jpg"):
            #    im = ImageGetter(self.id, title)
            # format the item
            #model = ""+title+"\n"+"\nYear: {y:10s}{r:50.0f}% affinity\n".format(y=year, r=self.ratio)
            model = "" + title + "\n" + "\n{r:0.0f}% affinity\n".format(r=self.ratio)
            #model += "Year: "+year+"\t\t\t\t\t"+str(self.ratio)+"% affinity"
            #print(model)
            return model

            # return "{t:50s} {r:8.0f}%\n".format(t=title, r=self.ratio)
        except IndexError:
            model = "" +self.title + "\n" + "\n{r:0.0f}% affinity\n".format(r=self.ratio)
            return model

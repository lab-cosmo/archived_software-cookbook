import json
import os
from myst_nb import glue
from PIL import Image

base_dir = "./COSMO_cookbook/"
max_grid = 4

examples = {
    "descriptors": [],
    "models": [],
    "analysis": [],
    "workflows": [],
    "contributing": [],
}


class Example:
    def __init__(self, folder):
        self.folder = folder
        self.meta_dict = self.test_meta()
        self.icon = (
            os.path.join(folder, self.meta_dict.get("icon"))
            if "icon" in self.meta_dict
            else "./square_logo.png"
        )

        self.title = self.meta_dict.get("title", "")
        self.category = self.test_category()

        if "link" in self.meta_dict:
            self.files = []
            self.link = self.meta_dict.get("link")
            self.title = self.title + " [EXTERNAL]"
        else:
            assert os.path.exists(
                os.path.join(base_dir, self.folder, "requirements.txt")
            )
            self.files = [
                os.path.join(folder, dp) for dp in self.meta_dict.get("files", [])
            ]
            self.link = self.files[0]

    def test_category(self):
        assert self.meta_dict.get("category") in examples.keys()
        return self.meta_dict.get("category")

    def test_meta(self):
        assert os.path.exists(os.path.join(base_dir, self.folder, "meta.json"))
        return json.load(open(os.path.join(base_dir, self.folder, "meta.json")))

    def build_thumbnail(self, num=None):
        return f'````{{grid-item}}\n[**{self.title}**]({self.link})\n```{{figure}} {self.icon}\n---\nclass: with-border\nalign: left\ntarget: {self.link.replace("ipynb", "html")}\nheight: 200px\n---\n```\n````\n'


for folder in os.listdir(os.path.join(base_dir, "examples")):
    if folder not in ["build_examples.py"]:
        example = Example(os.path.join("examples", folder))
        examples[example.category].append(example)

with open(os.path.join(base_dir, "_toc.yml"), "w") as outtoc:
    outtoc.write("format: jb-book\nroot: intro\nchapters:\n")
    for key, example_list in examples.items():
        outtoc.write("- file: " + key + "\n")
        existing_file = list(open(os.path.join(base_dir, f"{key}.md"), "r"))
        FLAG = "## Examples"
        with open(os.path.join(base_dir, f"{key}.md"), "w") as outf:
            for l in existing_file:
                if not l.startswith(FLAG):
                    outf.write(l)
                else:
                    outf.write(l)
                    break

            if len(example_list) > 0:
                section_added = False
                outf.write("`````{grid}\n")
                for example in example_list:
                    outf.write(example.build_thumbnail())
                    if not section_added:
                        outtoc.write("  sections: \n")
                        section_added = True
                    if "link" not in example.meta_dict:
                        for file in example.files:
                            outtoc.write("  - file: " + file + "\n")
                    else:
                        outtoc.write(
                            "  - url: "
                            + example.link
                            + "\n    title: "
                            + example.title
                            + "\n"
                        )
                outf.write("`````\n")

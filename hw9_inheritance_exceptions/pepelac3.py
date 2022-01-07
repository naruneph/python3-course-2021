def read_instructions():
    cfgs = []
    while True:
        cfg, stop = parse_instruction(input())
        cfgs.append(cfg)
        if stop:
            return cfgs


def parse_instruction(instr):
    class_cfg = {
        "name": None,
        "ancestors": [],
        "fields": [],
        "all_fields": []
    }

    items = instr.split(" ")

    if items[0].isupper() and len(items[0]) == 1:
        class_cfg["name"] = items[0]

        if items[1].isupper():
            class_cfg["ancestors"] = list(items[1])
        else:
            class_cfg["fields"] = list(items[1])

        if len(items) == 3:
            class_cfg["fields"] = list(items[2])
        
        return class_cfg, False

    if items[0].isupper() and len(items[0]) > 1:
        class_cfg["name"] = "PepelaC3"
        class_cfg["ancestors"] = list(items[0])
        class_cfg["fields"] = list(items[1])
        class_cfg["all_fields"] = list(items[2])
        return class_cfg, True


def create_class_from_config(cfg):
    ancestors = str(tuple(cfg['ancestors'])).replace("'", "")

    expr = f"class {cfg['name']}{ancestors}:\n"

    expr += "    def __init__(self):\n"

    expr += f"        super({cfg['name']}, self).__init__()\n"

    for f in cfg['fields']:
        expr += f"        self.{f} = ''\n"

    exec(expr, globals(), globals())


if __name__ == "__main__":
    try:
        cfgs = read_instructions()
        for c in cfgs:
            create_class_from_config(c)
   
        p = PepelaC3()

        for k in cfgs[-1]["all_fields"]:
            exec(f"p.{k}")

    except Exception:
        print("Incorrect")
    else:
        print("Correct")

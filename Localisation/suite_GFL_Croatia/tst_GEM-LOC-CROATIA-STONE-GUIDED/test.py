
def get_object_text(obj):
    texts = []

    attributes = (
        "text",
        "windowTitle",
        "placeholderText",
        "accessibleName",
        "title",
        "label",
        "caption",
        "displayText",
        "toolTip",
    )

    for attribute in attributes:
        try:
            value = getattr(obj, attribute)

            if callable(value):
                value = value()

            if value is not None:
                value = str(value).strip()

                if value and normalize(value):
                    texts.append(value)

        except Exception:
            pass

    return texts


def collect_screen_text(obj, collected=None, visited=None, depth=0):
    if collected is None:
        collected = []

    if visited is None:
        visited = set()

    if obj is None or depth > 30:
        return collected

    try:
        object_id = id(obj)

        if object_id in visited:
            return collected

        visited.add(object_id)

    except Exception:
        pass

    try:
        if not object.exists(obj):
            return collected
    except Exception:
        pass

    try:
        visible = obj.visible

        if not visible:
            return collected

    except Exception:
        pass

    for value in get_object_text(obj):
        if value not in collected:
            collected.append(value)

    try:
        children = object.children(obj)

        for child in children:
            collect_screen_text(
                child,
                collected,
                visited,
                depth + 1
            )

    except Exception:
        pass

    return collected


def build_screen_candidates(screen_texts):
    candidates = {}

    for text_value in screen_texts:
        cleaned = normalize(text_value)

        if cleaned:
            candidates[cleaned] = text_value

        for line in re.split(r"[\r\n]+", str(text_value)):
            cleaned_line = normalize(line)

            if cleaned_line:
                candidates[cleaned_line] = line.strip()

    return candidates

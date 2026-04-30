def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block:
            result.append(block)
    return result

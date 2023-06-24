from gensim.summarization import summarize

# Input text to be summarized
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum feugiat augue non ex dapibus tempus. Curabitur ac tincidunt dui. Nullam ac mi ut orci vestibulum mollis non non magna. Donec in velit risus. Cras ut mi varius, interdum orci in, elementum ipsum. Fusce consequat ligula id orci tempus, vitae maximus nisl iaculis. Integer scelerisque congue tristique. Ut quis tempus justo. Aenean ac diam malesuada, blandit odio eget, tincidunt nulla. Etiam nec ultrices sapien. Mauris eleifend lacus augue, vel interdum lacus scelerisque a. Nulla id purus varius, aliquet ex vitae, commodo mauris.

Phasellus feugiat enim vel lorem consectetur, a rutrum urna tincidunt. Cras blandit, quam ac efficitur euismod, ex risus luctus lectus, et convallis nisi metus non mauris. Donec et nisi lacinia, consectetur tellus sit amet, interdum lacus. Suspendisse finibus euismod arcu. Nulla eu nisi at est volutpat aliquam non nec mauris. Curabitur a elit ut lectus ultrices sagittis. Fusce semper laoreet enim, vitae rhoncus urna iaculis nec. Sed tincidunt nunc eget mi cursus, a iaculis ex tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur laoreet iaculis diam vel tristique.

Etiam at commodo velit. Aliquam non magna sapien. Morbi in orci vel libero auctor feugiat. Nulla ornare mi libero, vitae auctor ante scelerisque in. Vestibulum convallis vestibulum cursus. Nulla facilisi. Nunc vestibulum commodo neque vel hendrerit. In eget urna et mi consectetur rhoncus. Mauris vulputate, metus at cursus lobortis, diam nisi gravida est, id pulvinar sem orci eu nisi. Nulla facilisi. Sed varius enim nec erat facilisis iaculis. Curabitur et lorem in quam dictum semper. Sed laoreet tortor neque, sed finibus tellus sollicitudin sed. Suspendisse ornare leo id elit elementum, sed fermentum arcu volutpat. Aliquam eleifend felis eget dui elementum vestibulum. Phasellus faucibus felis sed quam tempor ultricies.
"""

# Summarize the text
summary = summarize(text)

# Print the summarized text
print(summary)

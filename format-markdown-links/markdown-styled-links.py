def create_markdown_link():
  """
  Takes a link and a display name from the user
  and prints a markdown-formatted link.
  """
  link = input("Enter the link: ")
  display_name = input("Enter the display name for the link: ")
  markdown_link = f"[{display_name}]({link})"
  print(markdown_link)

if __name__ == "__main__":
  create_markdown_link()

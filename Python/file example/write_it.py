print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("This would be line 3\n")
text_file.close()

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines = ["scores 1\n",
         "scores 2\n",
         "scores 3\n"]
text_file.writelines(lines)
text_file.close()

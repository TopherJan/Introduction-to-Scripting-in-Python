"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    short_string = line1 if len(line1) <= len(line2) else line2
    long_string = line1 if len(line1) > len(line2) else line2
    short_len = len(short_string)

    if line1 == line2:
        index = IDENTICAL
    elif short_string in long_string:
        index = short_len
    else:
        for idx in range(len(short_string)):
            if short_string[idx] != long_string[idx]:
                index = idx
                break

    return index

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if '\n' in line1 or '\n' in line2:
        return ""

    if '\r' in line1 or '\r' in line2:
        return ""

    if idx == -1 or idx > min(len(line1), len(line2)):
        return ""

    string_format = "{}\n{}\n{}\n".format(line1, ("=" * idx + "^"), line2)
    return string_format

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if not lines1 and not lines2:
        return (IDENTICAL, IDENTICAL)
    elif not lines1 or not lines2:
        return (0, 0)

    used_range = min(len(lines1), len(lines2))

    for index in range(used_range):
        diff_idx = singleline_diff(lines1[index], lines2[index])

        if diff_idx == IDENTICAL and index == used_range - 1 and len(lines1) == len(lines2):
            return (IDENTICAL, IDENTICAL)
        elif diff_idx == IDENTICAL and index == used_range - 1:
            return (used_range, 0)
        elif diff_idx == IDENTICAL:
            continue
        else:
            return (index, diff_idx)

    return None

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    data_file = open(filename, "rt")
    data = data_file.read().splitlines()
    data_file.close()
    return data

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    index, diff_idx = multiline_diff(file1, file2)

    if len(open(filename1).read()) == 0 and len(open(filename2).read()) == 0:
        return "No differences\n"
    elif len(open(filename1).read()) == 0:
        return "Line 0:\n" + "{0}\n{1}\n{2}\n".format("", "^", file2[0])
    elif len(open(filename2).read()) == 0:
        return "Line 0:\n" + "{0}\n{1}\n{2}\n".format(file1[0], "^", "")

    if index == diff_idx == -1:
        return "No differences\n"
    else:
        string_format = singleline_diff_format(file1[index], file2[index], diff_idx)
        return f"Line {index}:\n{string_format}"
    return string_format

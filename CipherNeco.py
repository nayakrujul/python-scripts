def encode(msg, key):

  msg, key = msg.upper().replace(" ", ""), key.upper()

  if not ( len(msg) > len(key) and len(key) > 0 ) :
    return False
  
  sorted_key = "".join(sorted(list(key)))
  length = len(sorted_key)

  msg_list = []

  for times in range(length):
    msg_list.append([key[times]])

  y = 0
  for x in range(len(msg)):

    msg_list[y].append(msg[x])
    y += 1

    if y >= length:
      y -= length

  for i in msg_list:

    if len(i) < len(msg_list[0]):
      i.append(" ")

  new_list = []

  for m in sorted_key:

    for n in range(len(msg_list)):

      if msg_list[n][0] == m:
        new_list.append(msg_list[n])
  
  for p in range(len(new_list)):

    new_list[p].pop(0)
  
  final_list = []

  for q in new_list:

    final_list.append(q[0])
  
  for r in new_list:

    final_list.append(r[1])
  
  return "".join(final_list)
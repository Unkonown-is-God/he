with open ('dics/emotion.txt','r',encoding='utf-8') as f:
  lines=[x for x in f.read().splitlines() if x]#リスト内表記で検索
  l=len(lines)
  parts=[lines[x].split(':') for x in range(l)]
  print(parts)
def main():
    f = open("Portfolio.toc",'r')
    s = f.read().split("\n")
    l = []
    l.append(s[0])
    asdf = '\contentsline {section}{Cover Letter}{1}{}\n\contentsline {section}{Resume}{2}{}'
    l.append(asdf)
    l += s[1:]
    final = '\n'.join(l)
    g = open("Portfolio.toc",'w')
    g.write(final)
    f.close()
    g.close()

main()
    

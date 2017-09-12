import sys, os, libxml2

def segv_test():
    s = "<html><body><div><a><a></a></a><a></a></div></body></html>"
    options = libxml2.HTML_PARSE_RECOVER + \
              libxml2.HTML_PARSE_NOERROR + \
              libxml2.HTML_PARSE_NOWARNING
    doc = libxml2.htmlReadDoc(s, None, 'utf-8', options).doc
    ctxt = doc.xpathNewContext()
    nodes = ctxt.xpathEval('//body/node()')
    nodes.reverse()
    for note in nodes:
        nexts = note.xpathEval('node()')
        note.unlinkNode()
        note.freeNode() 
        nexts[0].unlinkNode()
        nexts[0].freeNode()  

#free twice will segment fault

def main():
    segv_test()

if __name__ == "__main__":
    main()

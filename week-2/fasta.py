#!/usr/bin/env python

"""
Parse every FASTA record from a file and print
"""

import sys

class FASTAReader(object):
    
    def __init__( self, input_file ):
        self.file = input_file
        self.last_ident = None
        
    def __iter__( self ):
        return self
            
    def next( self ):
        # If this is the first call / first sequence
        if self.last_ident is None:    
            line = self.file.readline()
            # Verify it is a header line
            assert line.startswith(">")

            # Extract identifer 
            # ident = line.split()[0].lstrip(">")
            ident = line.split()[0][1:]
        # If we have been called before / seen a sequence before
        else:
            ident = self.last_ident

        sequences = []

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_ident = line.split()[0][1:]
                break
            elif line == "":
                if sequences:
                    return ident, "".join( sequences ) 
                raise StopIteration
            else:
                sequences.append( line )
        
        return ident, "".join( sequences )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
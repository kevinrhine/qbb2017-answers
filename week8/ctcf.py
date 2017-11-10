#!/usr/bin/env python

import sys
import numpy as np

def hifivedata():
    data = np.load( 'nora_ctcf.npz' )
    return data[ '0.forward' ], data[ '0.reverse' ], data[ '0.enrichment' ]

def ctcfbinding():
    ctcf_sites = []
    for line in open( sys.argv[1] ):
        line = line.rstrip('\r\n').split( '\t' )
        if line[0] == 'chrX':
            ctcf_sites.append( line[1] )
    return ctcf_sites
    
def primerdictionary():
    dictionary = {}
    for line in open( sys.argv[2] ):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == '#chr':
            pass
        else:
            dictionary[ line[1] + '_' + line[2] ] = line[3]
    return dictionary

def ctcf_indices( primers, ctcf_sites ):
    bank = []
    for i, each in enumerate( primers ):
        start, stop = int( each[0] ), int( each[1] )
        for site in ctcf_sites:
            if int( site ) >= start and int( site ) <= stop:
                bank.append( i )
                break
    return bank

def ixn_pairs( fwd_ind, rev_ind, enr ):
    bank_fwd, bank_rev = [], []
    for fwd in fwd_ind:
        top_rev, top = None, 0.
        for rev in rev_ind:
            if float( enr[ fwd ][ rev ] ) > top:
                top_rev = rev
                top = float( enr[ fwd ][ rev ] )
        bank_fwd.append( ( fwd, top_rev ) )
    for rev in rev_ind:
        top_for, top = None, 0.
        for fwd in fwd_ind:
            if float( enr[ fwd ][ rev ] ) > top:
                top_for = fwd
                top = float( enr[ fwd ][ rev ] )
        bank_rev.append( ( top_for, rev ) )
    return bank_fwd, bank_rev

def name_ixns( fwd, rev, pairs, dictionary, direction ):
    for ixn in pairs:
        fw_key = str( fwd[ ixn[0] ][0] ) + '_' + str( fwd[ ixn[0] ][1] )
        rv_key = str( rev[ ixn[1] ][0] ) + '_' + str( rev[ ixn[1] ][1] )
        if direction == 'fwd':
            print '%s\t%s' % ( dictionary[ fw_key ], dictionary[ rv_key ] )
        else:
            print '%s\t%s' % ( dictionary[ rv_key ], dictionary[ fw_key ] )
def main():
    ctcf_sites = ctcfbinding()
    fwd, rev, enr = hifivedata()
    dictionary = primerdictionary()
    fwd_ind, rev_ind = ctcf_indices( fwd, ctcf_sites ), ctcf_indices( rev, ctcf_sites )
    bank_fwd, bank_rev = ixn_pairs( fwd_ind, rev_ind, enr )
    print 'Top interactions with forward primers:'
    name_ixns(fwd, rev, bank_fwd, dictionary, 'fwd' )
    print '\nTop interactions with reverse primers:'
    name_ixns(fwd, rev, bank_rev, dictionary, 'rev' )
        
main()
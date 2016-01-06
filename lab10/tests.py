
"""
file: tests.py
description: Verify  LinkedHashTable class implementation
author: ds5930@cs.rit.edu Deepak Sharma
author: mj2997@cs.rit.edu Mayank Jain
"""
from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set:
        print( word, end=" " )
    print()

def test1():
    """
    This Test add 10 elements in has map and remove all of them to check the:
     Size after and before removal
     Contains after and before the removal
     Note: By removing all elements we also covered the testing of re-hashing and downsizing of
     hash table
    :return: None
    """
    print("\n Test First \n: ")
    table = LinkedHashTable()
    table.add( "brain" )
    table.add( "cathy" )
    table.add( "surya" )
    table.add( "anurag" )
    table.add( "deepak" )
    table.add( "sri" )
    table.add( "nora" )
    table.add( "arpit" )
    table.add( "avinav" )
    table.add( "7102198" )

    print_set( table )
    print("Size of the set: " + str(table.size))
    print( "'rit' in table?", table.contains( "rit" ) )
    print( "'anurag' in table?", table.contains( "anurag" ) )
    print( "'7102198' in table?", table.contains( "7102198" ) )


    table.remove( "deepak" )
    table.remove( "sri" )
    table.remove( "nora" )
    table.remove( "7102198" )
    table.remove( "brain" )
    table.remove( "cathy" )
    table.remove( "surya" )
    table.remove( "anurag" )
    table.remove( "arpit" )
    table.remove( "avinav" )

    print_set( table )
    print("Size " + str(table.size))
    print( "'avinav' in table?", table.contains( "avinav" ) )
    print( "'rit' in table?", table.contains( "rit" ) )
    print( "'anurag' in table?", table.contains( "anurag" ) )



def test2():
    """
    This test try to insert duplicate values in linked  hash map and check size of the hash map
    by this test we can check logical implementation of add method.
    :return:
    """
    print("\nTest Second  \n:")
    table = LinkedHashTable()
    table.add( "deepak" )
    table.add( "sri" )
    table.add( "nora" )
    table.add( "emily" )
    table.add( "brain" )
    table.add( "cathy" )
    table.add( "surya" )
    table.add( "anurag" )
    table.add( "sahil" )
    table.add( "lokesh" )
    table.add( "payal" )
    table.add( "hanna" )
    table.add( "surya" )
    table.add( "anna" )
    table.add( "arpit" )
    table.add( "avinav" )

    # adding same element multiple times for checking
    #logical implementation of add method
    table.add( "anna" )
    table.add ( "brain" )
    table.add ( "deepak" )
    table.add ( "nora" )
    table.add( "hanna" )
    table.add( "surya" )
    table.add( "anna" )

    print_set( table )
    print("Size " + str(table.size))

    print( "'deepak' in table?", table.contains( "deepak" ) )
    print( "'sri' in table?", table.contains( "sri" ) )
    print( "'nora' in table?", table.contains( "nora" ) )
    print( "'emily' in table?", table.contains( "emily" ) )
    print( "'hanna' in table?", table.contains( "hanna" ) )
    print( "'surya' in table?", table.contains( "surya" ) )
    print( "'anna' in table?", table.contains( "anna" ) )




def test3():
    """
    This Test check remove Functionality of the hash map
    add 10 elements
    check size
    check contains
    remove 3 elements
    check size
    check contains
    remove element which was already removed to check exception
    :return:
    """
    print("\nTest three : \n")
    table = LinkedHashTable(1)
    table.add( "deepak" )
    table.add( "sri" )
    table.add( "nora" )
    table.add( "rit" )
    table.add( "sahil" )
    table.add( "lokesh" )
    table.add( "payal" )
    table.add( "hanna" )
    table.add( "surya" )
    table.add( "anna" )

    print_set( table )
    print("Size " + str(table.size))

    print( "'hanna' in table?", table.contains( "hanna" ) )
    print( "'surya' in table?", table.contains( "surya" ) )
    print( "pearl(Not Inserted)  in table?", table.contains( "pearl" ) )
    print( "'deepak' in table?", table.contains( "deepak" ) )
    print( "'rit' in table?", table.contains( "rit" ) )
    print( "'anurag'(Not Inserted) in table?", table.contains( "anurag" ) )
    print("Size " + str(table.size))

    table.remove( "hanna" )
    table.remove( "surya" )
    table.remove( "deepak" )

    print("Removed: deepak surya and hanna")
    print_set( table )
    print("Size " + str(table.size))
    print( "'deepak' in table?", table.contains( "deepak" ) )
    print( "'surya' in table?", table.contains( "surya" ) )
    print( "'hanna' in table?", table.contains( "hanna" ) )

    print("Re-Removing an element: Deepak (already removed) should raise exception")
    try:
        table.remove("deepak")
    except Exception as details:
        print("Exceptions was raise :" + str(details))
        print(details.__str__())




if __name__ == '__main__':
    test1()
    test2()
    test3()


import csv
import os
import pandas as pd

#
# Type annotations for REL data storage
#
Row = tuple
Attrset = set[str]
Attrlist = list[str]
FD = tuple[Attrset, Attrset]

class REL:
    "A class that represents a relation with functional dependencies"
    def __init__(
            self,
            attributes: Attrlist,
            *,
            rows:list[Row]|None=None,
    ):
        "Constructs a relation, with no FDs"
        self.attributes = list(attributes)
        self.fds: list[FD] = []
        self.candidate_keys: list[Attrset] = []
        self.rows: list[Row] = list(set(rows)) if rows else []

    def __repr__(self):
        return f"R({','.join(self.attributes)})"
    
    def __str__(self):
        return repr(self)

    def df(self):
        "Shows the relation as a Pandas dataframe that is always sorted by values"

        # print FDs
        if self.fds:
            for (lhs, rhs) in self.fds:
                lhs = ", ".join(sorted(lhs))
                rhs = ", ".join(sorted(rhs))
                print(f"{lhs} -> {rhs}")
        else:
            print("No FDs.")

        # construct Pandas dataframe
        df = pd.DataFrame(data=self.rows, columns=self.attributes)
        return df.sort_values(by=self.attributes).reset_index(drop=True)

    #
    # TODO
    #
    def __eq__(self, another: 'REL')->bool:
        """
        Check if two relations are equal with x == y.
        The relation equality is insensitive to the order of the attributes
        nor the order of the tuples.
        """
        

    
    #
    # TODO
    #
    def satisfies(self, fd: FD)->bool:
        """
        Determine if REL satisfies `fd`
        """
        ...
    
    #
    # TODO
    #
    def add_fd(self, fd: FD):
        """
        Add given fd to REL.
        - If REL does not satisfy `fd`, throw an exception.
        - If `fd` has unknown attributes in left or right side, throw an exception
        """
        ...
    
    #
    # TODO
    #
    def closure(self, attrset: Attrset)->Attrset:
        """
        Compute the closure of the given attribute set `attrset` using the FDs
        of the REL.
        """
        ...

    #
    # TODO
    #
    def bcnf_violations(
        self,
    )->list[FD]:
        """
        return a list of FD that violate the BCNF condition
        """
        ...







#
# TODO
#
def load_csv(
    csv_file: str,
):
    """
    Load the relation from a given CSV file.  The first row is the attribute names.
    """
    with open(csv_file, 'r') as f:
        rows = []
        reader = csv.reader(f)
        for row in reader:
            rows.append(tuple(row))
        return REL(attributes=list(rows[0]), rows=rows[1:])

#
# TODO
#
def project(
    s: REL,
    attributes: list[str],
)->REL:
    """
    Perform projection of REL to the given `attributes`
    """
    ...


#
# TODO
#
def natural_join(
    s: REL,
    t: REL
)->REL:
    """
    Performs natural join between `s` and `t`.
    The attributes must follow the order of attributes of `s`, followed by
    the attributes in `t` that are not already included in the attributes of `s`.
    """
    ...

#
# TODO
#
def bcnf_decompose(s: REL) -> list[REL]:
    """
    Performs BNCF decomposiiton of `s`.  This needs to be done recursively.
    """
    ...
def schema_str(rel):
    lines = [f"R({','.join(sorted(rel.attributes))})"]
    for fd in rel.fds:
        lines.append(
            f"    FD: {fd_str(fd)}"
        )
    return "\n".join(lines)

def fd_str(fd):
    lhs, rhs = fd
    return f"{','.join(sorted(lhs))} -> {','.join(sorted(rhs))}"
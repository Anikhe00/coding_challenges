function dnaStrand(dna) {
  const reference = { A: "T", T: "A", C: "G", G: "C" };

  complementary = dna
    .split("")
    .map((n) => reference[n])
    .join("");

  return complementary;
}

// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package twofer implements the two-fer sharing phrase.
package twofer

// ShareWith returns a sharing phrase with the given name, defaulting to "you".
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return "One for " + name + ", one for me."
}

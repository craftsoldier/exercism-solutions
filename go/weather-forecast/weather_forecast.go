// Package weather provides weather forecasting functionality for Goblinocus.
package weather

// CurrentCondition holds the current weather condition.
var CurrentCondition string

// CurrentLocation holds the current city or location.
var CurrentLocation string

// Forecast returns a weather forecast message for the given city and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}

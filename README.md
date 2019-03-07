# Bike Diagnostic And Prognositic Toolkit

We provide a knowledge driven approach to understanding what is wrong with your bicycle and then providing suitable resolutions. Given a list of issues, particular parts of the bicycle have, we are able to provide a suitable list of resolutions for those issues.

1. To run and tinker with the toolkit we require the installation of **Companion**.
2. Clone the repository locally.
3. When you have installed Companion, start a session with a username and upload the `results.krf` file to the 
`interaction-manager`.
4. Once you have uploaded the file to Companion, you may search the Knowledge Base for the microtheory `KRR-Winter2019FactsMt` and the associated facts/rules in it to browse the microtheory we will be using.
5. To query the Knowledge Base:
     1. Navigate to the `Query` tab.
     2. Enter the query as: 
        ```
        (partOfRequiredSymptoms (TheSet (SymptomFn ?condition1 ?part1) (SymptomFn ?condition2 ?part2))
        ?required ?resolutions)
        ```

        1. Where `SymptomFn` is a function that returns a ProblemSymptom to the predicate formulated by the pairing of a condition and 
        a bike part, `?condition1` is the condition of bike part `?part1`, and `?condition2` is the condition of 
        bike part`?part2`, and so on. 
        2. The `?required` variable will return the set of required symptoms for a list of
        `resolutions` given the provided list of parts and associated conditions.
        3. If an incomplete list of conditions and parts are provided, such that the set of symptoms to be resolved by a 
        particular list of resolutions is incomplete, the query will return a list of proposed condition and part pairings
        that will be resolved by possible resolutions as a questioning system to help the user look at certain other problem 
        areas on the bicycle.

### Example Query

`(partOfRequiredSymptoms (TheSet (SymptomFn Rubbing BrakePad)) ?required ?resolutions)`

## Need to remember to...

- [x] Create a basic outputter and slot it in
- [ ] Pick a state graph display of some sort
- [ ] Implement various states (including input/output control flow)
    - Reference [this](https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module)
- [ ] Implement json control map parser
- [ ] Logging. How?
- [ ] Add "Context" member
- [ ] Presentation Flow
- [ ] Caught between templatized node generation and just coding it returning the next node to the state machine
    - I honestly think that it's simpler to just return the next state. Then the application becomes a list of states 
    - An error state, for instance, can return a basic landing page based on the `current_path` variable in the State Payload

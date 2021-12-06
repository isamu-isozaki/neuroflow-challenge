/*
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-05T23:17:20.064Z
Modified: !date!
Modified By: modifier
*/
import React, { useState } from "react";
import { Spacer, Text, Button, Flex, InputGroup, NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper} from "@chakra-ui/react";
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createMood } from 'app/store/mood';

function Mood({
    moods,
    createMood
}) {
    const [nextMood, setNextMood] = useState(0)
    const moodElems = moods.map(mood => {
        return (
            <Text key={mood.id}>mood: {mood.mood} streak: {mood.streak}</Text>
        )
    })
    return (
        <Flex direction='column' justify='center' align='center' height='100%'>
            <Spacer />
            <Flex direction='row'>
                <Spacer />
                <Flex direction='column'>
                    {moodElems}
                    <InputGroup justifyContent='center' marginTop={5}>
                        <NumberInput onChange={(val) => setNextMood(val)} min={0} max={10}>
                            <NumberInputField />
                            <NumberInputStepper>
                                <NumberIncrementStepper />
                                <NumberDecrementStepper />
                            </NumberInputStepper>
                        </NumberInput>
                    </InputGroup>
                    <Button onClick={()=>createMood(nextMood)} marginTop={5}>Submit</Button>
                </Flex>
                <Spacer />
            </Flex>
            <Spacer />
        </Flex>
    )
}


Mood.propTypes = {
    moods: PropTypes.array,
    createMood: PropTypes.func,
}
const mapStateToProps = (state) => ({
    moods: state.mood.moods,
});
  
export default connect(
    mapStateToProps, 
    {
        createMood,
    },
)(Mood);
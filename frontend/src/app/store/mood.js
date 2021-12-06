/*
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-08-28T17:30:44.844Z
Modified: !date!
Modified By: modifier
*/

import {
    postMood,
} from 'app/api/mood';
import _ from 'lodash'
import {
    LOGOUT_SUCCESS
} from 'app/store/auth';
import { ControlPointDuplicateOutlined } from '@material-ui/icons';
export const CREATE_MOOD_SUCCESS = 'CREATE_MOOD_SUCCESS';
export const MOOD_FAIL = 'MOOD_FAIL';





const initialState = {
    isInitializing: true,
    moods: [],
    error: false,
};

export default function moodReducer(state = initialState, 
{type, payload}) 
{
    switch (type) {
        case CREATE_MOOD_SUCCESS: {
            const { mood } = payload
            return {...state, moods: [...state.moods, mood]};
        }
        case MOOD_FAIL: {
            return state
        }
        default:
            return state;
    }
}

export function createMood(moodVal) {
    return async (dispatch, getState) => {
        try {
            const { token } = getState().auth
            const payload = await postMood(moodVal, token)
            const { mood } = payload
            dispatch({ type: CREATE_MOOD_SUCCESS, payload: { mood } });
        }
        catch (e) {
            console.log(e)
            dispatch({ type: MOOD_FAIL, payload: {} });
            return e
        }
    }
}
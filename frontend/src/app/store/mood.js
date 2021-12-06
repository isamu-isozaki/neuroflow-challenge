/*
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-08-28T17:30:44.844Z
Modified: !date!
Modified By: modifier
*/

import {
    postMood,
    getMoods
} from 'app/api/mood';
import _ from 'lodash'
import {
    LOGOUT_SUCCESS
} from 'app/store/auth';
export const LOAD_MOODS_SUCCESS = 'LOAD_MOODS_SUCCESS';
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
        case LOAD_MOODS_SUCCESS: {
            const {moods} = payload
            return {...state, moods, isInitializing: false}
        }
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

export function loadMoods() {
    return async (dispatch, getState) => {
        try {
            const { token } = getState().auth
            const payload = await getMoods(token)
            const { moods } = payload
            dispatch({ type: LOAD_MOODS_SUCCESS, payload: { moods } });
        }
        catch (e) {
            console.log(e)
            dispatch({ type: MOOD_FAIL, payload: {} });
            dispatch({ type: LOGOUT_SUCCESS, payload: {} })
            return e
        }
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
            dispatch({ type: LOGOUT_SUCCESS, payload: {} })
            return e
        }
    }
}
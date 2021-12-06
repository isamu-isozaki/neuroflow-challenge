/**
 * Author: Isamu Isozaki
 * User Redux
 */
import {getToken, postUser} from 'app/api/users';

const SET_INITIALIZING = 'SET_INITIALIZING';
const SET_LOGGED_IN = 'SET_LOGGED_IN';
const SET_EMAIL = 'SET_EMAIL';
const LOAD_TOKEN_SUCCESS = 'LOAD_TOKEN_SUCCESS';
export const LOGOUT_SUCCESS = 'LOGOUT_SUCCESS';
const USER_FAIL = 'USER_FAIL';



const initialState = {
  isInitializing: true,
  isLoggedIn: false,
  email: null,
  token: null
};

export default function authReducer(state = initialState, {type, payload}) {
  switch (type) {
    case SET_INITIALIZING:
      return {...state, isInitializing: true};
    case SET_LOGGED_IN:
      return {...state, isLoggedIn: payload.isLoggedIn};
    case SET_EMAIL: {
      const {email} = payload
      return {...state, email}
    }
    case LOAD_TOKEN_SUCCESS: {
      const {token} = payload

      return {...state, token, isInitializing: false}
    }
    case LOGOUT_SUCCESS: {
      return {...state, token: null, email: null, isInitializing: true}
    }
    case USER_FAIL: {
      return state;
    }
    default:
      return state;
  }
}


export function doSignup(email, first_name, last_name, password) {
  return async dispatch => {
    try {
      const {token} = await postUser(email, first_name, last_name, password);
      await dispatch({type: SET_EMAIL, payload: {email}});
      await dispatch({type: LOAD_TOKEN_SUCCESS, payload: {token}});
    }
    catch (e) {
      dispatch({ type: USER_FAIL, payload: {} });
      return e
    }
  };
}

export function doLogin(email, password) {
  return async dispatch => {
    try {
      const {token} = await getToken(email, password);
      await dispatch({type: SET_EMAIL, payload: {email}});
      await dispatch({type: LOAD_TOKEN_SUCCESS, payload: {token}});
    }
    catch (e) {
        dispatch({ type: USER_FAIL, payload: {} });
        return e
    }
  };
}

export function doLogout() {
  return async dispatch => {
    try {
      await dispatch({type: LOGOUT_SUCCESS, payload: {}});
    }
    catch (e) {
        dispatch({ type: USER_FAIL, payload: {} });
        return e
    }
  };
}

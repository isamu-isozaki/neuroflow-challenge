/**
 * Author: Isamu Isozaki
 * Combine reducers
 */
import {combineReducers} from 'redux';
import authReducer from './auth';
import moodReducer from './mood';



export default combineReducers({
  auth: authReducer,
  mood: moodReducer
});

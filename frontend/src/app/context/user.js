import { createContext } from 'react';

export const ContextValue = {
    username: '',
    email: '',
    phone:'',
    password: '',
    confirmPassword: '',
};

export const AuthContext = createContext(null);
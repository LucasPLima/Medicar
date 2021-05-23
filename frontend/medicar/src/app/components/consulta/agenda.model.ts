import { Medico } from "./medico.model";

export interface Agenda{
    id:number
    medico:Medico
    dia:string
    horarios:string[]
}
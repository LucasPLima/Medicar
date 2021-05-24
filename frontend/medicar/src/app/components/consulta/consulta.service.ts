import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { EMPTY, Observable } from 'rxjs';
import { Consulta } from './consulta.model';
import { environment } from '../../../environments/environment';
import { catchError, map } from 'rxjs/operators';
import { NotificationService } from 'src/app/util/notification.service';
import { AuthService } from 'src/app/auth/auth.service';
import { Especialidade } from './especialidade.model';
import { Medico } from './medico.model';
import { Agenda } from './agenda.model';
import { ConsultaCreate } from './consulta-create.model';

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {

  constructor(private http: HttpClient,
              private authService: AuthService,
              private notificationService:NotificationService) { }
  

  errorHandler(e:any):Observable<any>{
    const status = e.status.toString()
    
    if (status.charAt(0)==='4'){
      const responseError = e.error
      const errorObject = Object.keys(responseError)[0]
      const messageError= responseError[errorObject][0]
      this.notificationService.showWarningMsg(messageError)
      //message.dismiss()
    }else{
      this.notificationService.showErrorMsg("Erro de comunicação com o servidor.")
    }
    
    return EMPTY;
  }

  list():Observable<Consulta[]>{
    return this.http.get<Consulta[]>(`${environment.apiURL}/consultas/`,
                                    {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                                    .pipe(
                                    map((obj) => obj),
                                    catchError((e)=>this.errorHandler(e)))
  }

  getEspecialidades():Observable<Especialidade[]>{
    return this.http.get<Especialidade[]>(`${environment.apiURL}/especialidades/`,
                                          {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                                          .pipe(
                                            map((obj)=>obj),
                                            catchError((e)=>this.errorHandler(e))
                                          )
  }
  getMedicosByEspecialidade(especialidadeId:number):Observable<Medico[]>{
    return this.http.get<Medico[]>(`${environment.apiURL}/medicos?especialidade=${especialidadeId}`,
                                          {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                                          .pipe(
                                            map((obj)=>obj),
                                            catchError((e)=>this.errorHandler(e))
                                          )
  }
  getAgendas():Observable<Agenda[]>{
    return this.http.get<Agenda[]>(`${environment.apiURL}/agendas/`,
                                          {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                                          .pipe(
                                            map((obj)=>obj),
                                            catchError((e)=>this.errorHandler(e))
                                          )
  }

  createConsulta(consulta:ConsultaCreate):Observable<Consulta>{
    return this.http.post<Consulta>(`${environment.apiURL}/consultas/`, 
                             consulta,
                            {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                            .pipe(
                              map((obj)=>obj),
                              catchError((e)=>this.errorHandler(e))
                            )
  }

  deleteConsultaById(consulta_id:number):Observable<any>{
    return this.http.delete(`${environment.apiURL}/consultas/${consulta_id}`,
                            {headers:{"Authorization":`Token ${this.authService.getToken()}` }})
                            .pipe(
                              map((obj)=>obj),
                              catchError((e)=>this.errorHandler(e))
                            )
  }


}

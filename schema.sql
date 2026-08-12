-- Supabase Database Schema for SnapClass AI Attendance App
-- Copy and run this script in your Supabase SQL Editor (Dashboard -> SQL Editor -> New Query)

-- 1. Teachers Table
CREATE TABLE IF NOT EXISTS public.teachers (
    teacher_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Students Table
CREATE TABLE IF NOT EXISTS public.students (
    student_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    face_embedding JSONB,
    voice_embedding JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Subjects Table
CREATE TABLE IF NOT EXISTS public.subjects (
    subject_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subject_code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    section TEXT NOT NULL,
    teacher_id BIGINT NOT NULL REFERENCES public.teachers(teacher_id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Subject Students (Enrollments)
CREATE TABLE IF NOT EXISTS public.subject_students (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_id BIGINT NOT NULL REFERENCES public.students(student_id) ON DELETE CASCADE,
    subject_id BIGINT NOT NULL REFERENCES public.subjects(subject_id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(student_id, subject_id)
);

-- 5. Attendance Logs
CREATE TABLE IF NOT EXISTS public.attendance_logs (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_id BIGINT NOT NULL REFERENCES public.students(student_id) ON DELETE CASCADE,
    subject_id BIGINT NOT NULL REFERENCES public.subjects(subject_id) ON DELETE CASCADE,
    timestamp TEXT NOT NULL,
    is_present BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Disable Row Level Security (RLS) for simple direct API access from Streamlit
ALTER TABLE public.teachers DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.students DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.subjects DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.subject_students DISABLE ROW LEVEL SECURITY;
ALTER TABLE public.attendance_logs DISABLE ROW LEVEL SECURITY;

-- Reload PostgREST Schema Cache
NOTIFY pgrst, 'reload schema';
